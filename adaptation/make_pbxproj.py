#!/usr/bin/env python3
"""为 Compositor 重新生成一份 Xcode 15 能打开的 project.pbxproj。

原工程用的是 objectVersion 77 + PBXFileSystemSynchronizedRootGroup（Xcode 16 起才有），
Xcode 15.2 无法读取。这里把目录树展开成显式的文件引用，并把部署目标降到 14.0。

用法： python3 make_pbxproj.py <repo_root>
"""
import hashlib
import os
import sys

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
APP_DIR = os.path.join(ROOT, "Compositor")

# 沿用原工程的 UUID，这样已有的 xcscheme 不用改
PROJ = "8F311F91304F03BB0017D14F"
MAIN_GROUP = "8F311F90304F03BB0017D14F"
PRODUCTS_GROUP = "8F311F9A304F03BB0017D14F"
APP_GROUP = "8F311F9B304F03BB0017D14F"          # 原来指向同名同步文件夹
APP_TARGET = "8F311F98304F03BB0017D14F"
APP_PRODUCT = "8F311F99304F03BB0017D14F"
SOURCES_PHASE = "8F311F95304F03BB0017D14F"
FRAMEWORKS_PHASE = "8F311F96304F03BB0017D14F"
RESOURCES_PHASE = "8F311F97304F03BB0017D14F"
PROJ_CFG_LIST = "8F311F94304F03BB0017D14F"
PROJ_DEBUG = "8F311FB8304F03BC0017D14F"
PROJ_RELEASE = "8F311FB9304F03BC0017D14F"
APP_CFG_LIST = "8F311FBA304F03BC0017D14F"
APP_DEBUG = "8F311FBB304F03BC0017D14F"
APP_RELEASE = "8F311FBC304F03BC0017D14F"


def uuid(kind, key):
    return hashlib.md5(f"{kind}:{key}".encode()).hexdigest()[:24].upper()


def q(s):
    """pbxproj 里含有特殊字符的值要加引号。"""
    if s == "" or any(c in s for c in " /<>$@:;,+=") or s[0].isdigit():
        return '"%s"' % s.replace("\\", "\\\\").replace('"', '\\"')
    return s


def collect():
    """返回 (子目录名 -> 文件列表, 根目录文件列表)。"""
    dirs, root_files = {}, []
    for dirpath, dirnames, filenames in os.walk(APP_DIR):
        # .lproj 本地化目录整体作为一个资源（folder reference），不展开
        lprojs = [d for d in dirnames if d.endswith(".lproj")]
        dirnames[:] = [d for d in dirnames if not d.endswith(".lproj")]
        rel = os.path.relpath(dirpath, APP_DIR)
        entries = sorted(
            f for f in filenames
            if f != "Compositor-Bridging-Header.h" and not f.startswith(".")
        ) + sorted(lprojs)
        # 顶层还要带上资源目录（os.walk 会把 .xcassets 当目录走进去，单独处理）
        if rel == ".":
            root_files = entries
        else:
            if rel.split(os.sep)[0].endswith(".xcassets"):
                continue
            dirs[rel] = entries
    # 目录形式资源
    for name in sorted(os.listdir(APP_DIR)):
        if name.endswith(".xcassets"):
            root_files.append(name)
    return dirs, sorted(root_files)


FILE_TYPE = {
    ".swift": "sourcecode.swift",
    ".c": "sourcecode.c.c",
    ".h": "sourcecode.c.h",
    ".m": "sourcecode.c.objc",
    ".xcassets": "folder.assetcatalog",
    ".plist": "text.plist.xml",
    ".md": "net.daringfireball.markdown",
    ".metal": "sourcecode.metal",
}
COMPILE_EXT = {".swift", ".c", ".m", ".metal"}


def file_type(name):
    if name.endswith(".xcassets"):
        return "folder.assetcatalog"
    if name.endswith(".lproj"):
        return "folder"
    ext = os.path.splitext(name)[1]
    return FILE_TYPE.get(ext, "text")


def main():
    dirs, root_files = collect()

    file_refs, build_files, groups = [], [], []
    source_build_ids, resource_build_ids = [], []

    def add_files(files, group_key, prefix):
        """为一组文件建 fileRef / buildFile，返回 fileRef id 列表。"""
        ids = []
        for name in files:
            key = f"{prefix}/{name}"
            ref = uuid("ref", key)
            path = name
            file_refs.append(
                f"\t\t{ref} /* {name} */ = {{isa = PBXFileReference; "
                f"lastKnownFileType = {file_type(name)}; path = {q(path)}; sourceTree = \"<group>\"; }};"
            )
            ids.append((ref, name))
            ext = os.path.splitext(name)[1]
            if name.endswith(".lproj"):
                ext = ".lproj"  # 本地化目录进 Resources
            if ext in COMPILE_EXT:
                bf = uuid("bf", key)
                build_files.append(
                    f"\t\t{bf} /* {name} in Sources */ = {{isa = PBXBuildFile; fileRef = {ref} /* {name} */; }};"
                )
                source_build_ids.append((bf, name))
            elif ext in (".xcassets", ".lproj"):
                bf = uuid("bf", key)
                build_files.append(
                    f"\t\t{bf} /* {name} in Resources */ = {{isa = PBXBuildFile; fileRef = {ref} /* {name} */; }};"
                )
                resource_build_ids.append((bf, name))
        return ids

    root_ids = add_files(root_files, "root", "")

    child_ids = []
    for rel in sorted(dirs):
        name = rel.split(os.sep)[-1]
        gid = uuid("group", rel)
        ids = add_files(dirs[rel], rel, rel)
        children = ""
        for d in sorted(dirs):
            if os.path.dirname(d) == rel:
                children += f"\t\t\t\t{uuid('group', d)} /* {os.path.basename(d)} */,\n"
        for ref, fname in ids:
            children += f"\t\t\t\t{ref} /* {fname} */,\n"
        groups.append(
            f"\t\t{gid} /* {name} */ = {{\n\t\t\tisa = PBXGroup;\n\t\t\tchildren = (\n"
            f"{children}\t\t\t);\n\t\t\tpath = {q(name)};\n\t\t\tsourceTree = \"<group>\";\n\t\t}};"
        )
        child_ids.append((gid, name))

    root_children = ""
    for gid, name in child_ids:
        rel = next(d for d in dirs if d.split(os.sep)[-1] == name)
        if os.path.dirname(rel) == "":
            root_children += f"\t\t\t\t{gid} /* {name} */,\n"
    for ref, fname in root_ids:
        root_children += f"\t\t\t\t{ref} /* {fname} */,\n"

    groups.insert(0,
        f"\t\t{APP_GROUP} /* Compositor */ = {{\n\t\t\tisa = PBXGroup;\n\t\t\tchildren = (\n"
        f"{root_children}\t\t\t);\n\t\t\tpath = Compositor;\n\t\t\tsourceTree = \"<group>\";\n\t\t}};")

    sources = "\n".join(f"\t\t\t\t{bf} /* {n} in Sources */," for bf, n in source_build_ids)
    resources = "\n".join(f"\t\t\t\t{bf} /* {n} in Resources */," for bf, n in resource_build_ids)

    text = f"""// !$*UTF8*$!
{{
	archiveVersion = 1;
	classes = {{
	}};
	objectVersion = 56;
	objects = {{

/* Begin PBXBuildFile section */
{chr(10).join(build_files)}
/* End PBXBuildFile section */

/* Begin PBXFileReference section */
{chr(10).join(file_refs)}
\t\t{APP_PRODUCT} /* Compositor.app */ = {{isa = PBXFileReference; explicitFileType = wrapper.application; includeInIndex = 0; path = Compositor.app; sourceTree = BUILT_PRODUCTS_DIR; }};
/* End PBXFileReference section */

/* Begin PBXFrameworksBuildPhase section */
\t\t{FRAMEWORKS_PHASE} /* Frameworks */ = {{
\t\t\tisa = PBXFrameworksBuildPhase;
\t\t\tbuildActionMask = 2147483647;
\t\t\tfiles = (
\t\t\t);
\t\t\trunOnlyForDeploymentPostprocessing = 0;
\t\t}};
/* End PBXFrameworksBuildPhase section */

/* Begin PBXGroup section */
\t\t{MAIN_GROUP} = {{
\t\t\tisa = PBXGroup;
\t\t\tchildren = (
\t\t\t\t{APP_GROUP} /* Compositor */,
\t\t\t\t{PRODUCTS_GROUP} /* Products */,
\t\t\t);
\t\t\tsourceTree = "<group>";
\t\t}};
\t\t{PRODUCTS_GROUP} /* Products */ = {{
\t\t\tisa = PBXGroup;
\t\t\tchildren = (
\t\t\t\t{APP_PRODUCT} /* Compositor.app */,
\t\t\t);
\t\t\tname = Products;
\t\t\tsourceTree = "<group>";
\t\t}};
{chr(10).join(groups)}
/* End PBXGroup section */

/* Begin PBXNativeTarget section */
\t\t{APP_TARGET} /* Compositor */ = {{
\t\t\tisa = PBXNativeTarget;
\t\t\tbuildConfigurationList = {APP_CFG_LIST} /* Build configuration list for PBXNativeTarget "Compositor" */;
\t\t\tbuildPhases = (
\t\t\t\t{SOURCES_PHASE} /* Sources */,
\t\t\t\t{FRAMEWORKS_PHASE} /* Frameworks */,
\t\t\t\t{RESOURCES_PHASE} /* Resources */,
\t\t\t);
\t\t\tbuildRules = (
\t\t\t);
\t\t\tdependencies = (
\t\t\t);
\t\t\tname = Compositor;
\t\t\tproductName = Compositor;
\t\t\tproductReference = {APP_PRODUCT} /* Compositor.app */;
\t\t\tproductType = "com.apple.product-type.application";
\t\t}};
/* End PBXNativeTarget section */

/* Begin PBXProject section */
\t\t{PROJ} /* Project object */ = {{
\t\t\tisa = PBXProject;
\t\t\tattributes = {{
\t\t\t\tBuildIndependentTargetsInParallel = 1;
\t\t\t\tLastSwiftUpdateCheck = 1520;
\t\t\t\tLastUpgradeCheck = 1520;
\t\t\t\tTargetAttributes = {{
\t\t\t\t\t{APP_TARGET} = {{
\t\t\t\t\t\tCreatedOnToolsVersion = 15.2;
\t\t\t\t\t}};
\t\t\t\t}};
\t\t\t}};
\t\t\tbuildConfigurationList = {PROJ_CFG_LIST} /* Build configuration list for PBXProject "Compositor" */;
\t\t\tdevelopmentRegion = en;
\t\t\thasScannedForEncodings = 0;
\t\t\tknownRegions = (
\t\t\t\ten,
\t\t\t\tBase,
\t\t\t);
\t\t\tmainGroup = {MAIN_GROUP};
\t\t\tproductRefGroup = {PRODUCTS_GROUP} /* Products */;
\t\t\tprojectDirPath = "";
\t\t\tprojectRoot = "";
\t\t\ttargets = (
\t\t\t\t{APP_TARGET} /* Compositor */,
\t\t\t);
\t\t}};
/* End PBXProject section */

/* Begin PBXResourcesBuildPhase section */
\t\t{RESOURCES_PHASE} /* Resources */ = {{
\t\t\tisa = PBXResourcesBuildPhase;
\t\t\tbuildActionMask = 2147483647;
\t\t\tfiles = (
{resources}
\t\t\t);
\t\t\trunOnlyForDeploymentPostprocessing = 0;
\t\t}};
/* End PBXResourcesBuildPhase section */

/* Begin PBXSourcesBuildPhase section */
\t\t{SOURCES_PHASE} /* Sources */ = {{
\t\t\tisa = PBXSourcesBuildPhase;
\t\t\tbuildActionMask = 2147483647;
\t\t\tfiles = (
{sources}
\t\t\t);
\t\t\trunOnlyForDeploymentPostprocessing = 0;
\t\t}};
/* End PBXSourcesBuildPhase section */

/* Begin XCBuildConfiguration section */
{project_config(PROJ_DEBUG, "Debug")}
{project_config(PROJ_RELEASE, "Release")}
{target_config(APP_DEBUG, "Debug")}
{target_config(APP_RELEASE, "Release")}
/* End XCBuildConfiguration section */

/* Begin XCConfigurationList section */
\t\t{PROJ_CFG_LIST} /* Build configuration list for PBXProject "Compositor" */ = {{
\t\t\tisa = XCConfigurationList;
\t\t\tbuildConfigurations = (
\t\t\t\t{PROJ_DEBUG} /* Debug */,
\t\t\t\t{PROJ_RELEASE} /* Release */,
\t\t\t);
\t\t\tdefaultConfigurationIsVisible = 0;
\t\t\tdefaultConfigurationName = Release;
\t\t}};
\t\t{APP_CFG_LIST} /* Build configuration list for PBXNativeTarget "Compositor" */ = {{
\t\t\tisa = XCConfigurationList;
\t\t\tbuildConfigurations = (
\t\t\t\t{APP_DEBUG} /* Debug */,
\t\t\t\t{APP_RELEASE} /* Release */,
\t\t\t);
\t\t\tdefaultConfigurationIsVisible = 0;
\t\t\tdefaultConfigurationName = Release;
\t\t}};
/* End XCConfigurationList section */
	}};
	rootObject = {PROJ} /* Project object */;
}}
"""
    out = os.path.join(ROOT, "Compositor.xcodeproj", "project.pbxproj")
    with open(out, "w") as fh:
        fh.write(text)
    print(f"写出 {out}")
    print(f"  Swift/C 编译单元 {len(source_build_ids)} 个，资源 {len(resource_build_ids)} 个，文件引用 {len(file_refs)} 个")


def project_config(cid, name):
    debug = name == "Debug"
    extra = ""
    if debug:
        extra = """				DEBUG_INFORMATION_FORMAT = dwarf;
				ENABLE_TESTABILITY = YES;
				GCC_DYNAMIC_NO_PIC = NO;
				GCC_OPTIMIZATION_LEVEL = 0;
				GCC_PREPROCESSOR_DEFINITIONS = (
					"DEBUG=1",
					"$(inherited)",
				);
				MTL_ENABLE_DEBUG_INFO = INCLUDE_SOURCE;
				ONLY_ACTIVE_ARCH = YES;
				SWIFT_ACTIVE_COMPILATION_CONDITIONS = "DEBUG $(inherited)";
				SWIFT_OPTIMIZATION_LEVEL = "-Onone";
"""
    else:
        extra = """				DEBUG_INFORMATION_FORMAT = "dwarf-with-dsym";
				ENABLE_NS_ASSERTIONS = NO;
				MTL_ENABLE_DEBUG_INFO = NO;
				SWIFT_COMPILATION_MODE = wholemodule;
"""
    return f"""\t\t{cid} /* {name} */ = {{
\t\t\tisa = XCBuildConfiguration;
\t\t\tbuildSettings = {{
\t\t\t\tALWAYS_SEARCH_USER_PATHS = NO;
\t\t\t\tARCHS = arm64;
\t\t\t\tASSETCATALOG_COMPILER_GENERATE_SWIFT_ASSET_SYMBOL_EXTENSIONS = YES;
\t\t\t\tCLANG_ANALYZER_NONNULL = YES;
\t\t\t\tCLANG_ANALYZER_NUMBER_OBJECT_CONVERSION = YES_AGGRESSIVE;
\t\t\t\tCLANG_CXX_LANGUAGE_STANDARD = "gnu++20";
\t\t\t\tCLANG_ENABLE_MODULES = YES;
\t\t\t\tCLANG_ENABLE_OBJC_ARC = YES;
\t\t\t\tCLANG_ENABLE_OBJC_WEAK = YES;
\t\t\t\tCLANG_WARN_BLOCK_CAPTURE_AUTORELEASING = YES;
\t\t\t\tCLANG_WARN_BOOL_CONVERSION = YES;
\t\t\t\tCLANG_WARN_COMMA = YES;
\t\t\t\tCLANG_WARN_CONSTANT_CONVERSION = YES;
\t\t\t\tCLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS = YES;
\t\t\t\tCLANG_WARN_DIRECT_OBJC_ISA_USAGE = YES_ERROR;
\t\t\t\tCLANG_WARN_DOCUMENTATION_COMMENTS = YES;
\t\t\t\tCLANG_WARN_EMPTY_BODY = YES;
\t\t\t\tCLANG_WARN_ENUM_CONVERSION = YES;
\t\t\t\tCLANG_WARN_INFINITE_RECURSION = YES;
\t\t\t\tCLANG_WARN_INT_CONVERSION = YES;
\t\t\t\tCLANG_WARN_NON_LITERAL_NULL_CONVERSION = YES;
\t\t\t\tCLANG_WARN_OBJC_IMPLICIT_RETAIN_SELF = YES;
\t\t\t\tCLANG_WARN_OBJC_LITERAL_CONVERSION = YES;
\t\t\t\tCLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;
\t\t\t\tCLANG_WARN_QUOTED_INCLUDE_IN_FRAMEWORK_HEADER = YES;
\t\t\t\tCLANG_WARN_RANGE_LOOP_ANALYSIS = YES;
\t\t\t\tCLANG_WARN_STRICT_PROTOTYPES = YES;
\t\t\t\tCLANG_WARN_SUSPICIOUS_MOVE = YES;
\t\t\t\tCLANG_WARN_UNGUARDED_AVAILABILITY = YES_AGGRESSIVE;
\t\t\t\tCLANG_WARN_UNREACHABLE_CODE = YES;
\t\t\t\tCLANG_WARN__DUPLICATE_METHOD_MATCH = YES;
\t\t\t\tCOPY_PHASE_STRIP = NO;
\t\t\t\tDEAD_CODE_STRIPPING = YES;
\t\t\t\tDEVELOPMENT_TEAM = "";
\t\t\t\tENABLE_STRICT_OBJC_MSGSEND = YES;
\t\t\t\tENABLE_USER_SCRIPT_SANDBOXING = YES;
\t\t\t\tGCC_C_LANGUAGE_STANDARD = gnu17;
\t\t\t\tGCC_NO_COMMON_BLOCKS = YES;
\t\t\t\tGCC_WARN_64_TO_32_BIT_CONVERSION = YES;
\t\t\t\tGCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;
\t\t\t\tGCC_WARN_UNDECLARED_SELECTOR = YES;
\t\t\t\tGCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;
\t\t\t\tGCC_WARN_UNUSED_FUNCTION = YES;
\t\t\t\tGCC_WARN_UNUSED_VARIABLE = YES;
\t\t\t\tLOCALIZATION_PREFERS_STRING_CATALOGS = YES;
\t\t\t\tMACOSX_DEPLOYMENT_TARGET = 14.0;
\t\t\t\tMTL_FAST_MATH = YES;
\t\t\t\tSDKROOT = macosx;
\t\t\t\tSTRING_CATALOG_GENERATE_SYMBOLS = YES;
{extra}\t\t\t}};
\t\t\tname = {name};
\t\t}};"""


def target_config(cid, name):
    return f"""\t\t{cid} /* {name} */ = {{
\t\t\tisa = XCBuildConfiguration;
\t\t\tbuildSettings = {{
\t\t\t\tASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
\t\t\t\tASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;
\t\t\t\tCODE_SIGN_ENTITLEMENTS = Config/Compositor.entitlements;
\t\t\t\tCODE_SIGN_IDENTITY = "-";
\t\t\t\tCODE_SIGN_STYLE = Manual;
\t\t\t\tCOMBINE_HIDPI_IMAGES = YES;
\t\t\t\tCURRENT_PROJECT_VERSION = 41;
\t\t\t\tDEAD_CODE_STRIPPING = YES;
\t\t\t\tDEVELOPMENT_TEAM = "";
\t\t\t\tENABLE_APP_SANDBOX = YES;
\t\t\t\tENABLE_HARDENED_RUNTIME = YES;
\t\t\t\tENABLE_OUTGOING_NETWORK_CONNECTIONS = YES;
\t\t\t\tENABLE_PREVIEWS = YES;
\t\t\t\tENABLE_USER_SELECTED_FILES = readwrite;
\t\t\t\tGCC_OPTIMIZATION_LEVEL = 3;
\t\t\t\tGENERATE_INFOPLIST_FILE = YES;
\t\t\t\tINFOPLIST_FILE = Config/Info.plist;
\t\t\t\tINFOPLIST_KEY_LSApplicationCategoryType = "public.app-category.graphics-design";
\t\t\t\tINFOPLIST_KEY_NSHumanReadableCopyright = "";
\t\t\t\tLD_RUNPATH_SEARCH_PATHS = (
\t\t\t\t\t"$(inherited)",
\t\t\t\t\t"@executable_path/../Frameworks",
\t\t\t\t);
\t\t\t\tMARKETING_VERSION = 1.4.6;
\t\t\t\tPRODUCT_BUNDLE_IDENTIFIER = com.wonderassembly.compositor;
\t\t\t\tPRODUCT_NAME = "$(TARGET_NAME)";
\t\t\t\tSTRING_CATALOG_GENERATE_SYMBOLS = YES;
\t\t\t\tSWIFT_EMIT_LOC_STRINGS = YES;
\t\t\t\tSWIFT_OBJC_BRIDGING_HEADER = "Compositor/Compositor-Bridging-Header.h";
\t\t\t\tSWIFT_VERSION = 5.0;
\t\t\t}};
\t\t\tname = {name};
\t\t}};"""


if __name__ == "__main__":
    main()
