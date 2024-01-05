import sys

sys.path.insert(0, "/Users/oleavr/src/telco/build/telco-macos-universal/lib/python2.7/site-packages")

if __name__ == "__main__":
    from PyObjCTools import AppHelper

    AppHelper.runEventLoop()
