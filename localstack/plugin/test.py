import logging
import pkgutil
from typing import List

from localstack.plugin import PluginSpec
from localstack.plugin.collector import ModuleScanningPluginCollector, PluginCollector


def err(*args, **kwargs):
    print("ERROR", *args)


class SysPathPluginCollector(PluginCollector):
    def collect_plugins(self) -> List[PluginSpec]:
        for imp, module, ispackage in pkgutil.walk_packages(path=["./localstack"]):
            print(imp, module, ispackage)

        return []


def main():
    import localstack.cli.plugin

    print("CREATING EXTENSION MANAGER")
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger("botocore").setLevel(level=logging.ERROR)

    # collector = PackageFinderPluginCollector(exclude=('tests', 'tests.*',))
    collector = ModuleScanningPluginCollector([localstack.cli.plugin])
    print(collector.collect_plugins())


if __name__ == "__main__":
    main()
