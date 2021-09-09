from localstack.plugin.collector import EntryPointDict, PackageFinderPluginCollector


def find_plugins(where=".", exclude=(), include=("*",)) -> EntryPointDict:
    return PackageFinderPluginCollector(
        where=where, exclude=exclude, include=include
    ).get_entry_points()
