from conan.packager import ConanMultiPackager
import os, platform

if __name__ == "__main__":
    builder = ConanMultiPackager(
    reference = "libtins/3.5",
    username = "solvingj", 
    login_username = "solvingj",
    password = os.environ["CONAN_PASSWORD"],
    channel = "testing",
    upload = "https://api.bintray.com/conan/solvingj/public-conan")
    builder.run()