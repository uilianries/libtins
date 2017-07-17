from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(username="mfontanini")
    builder.add_common_builds(shared_option_name="libtins:shared")
    builder.run()
