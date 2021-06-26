import json
import urllib3
import warnings

# Default bStats charts to read
_default_charts = ["servers", "players", "onlineMode", "minecraftVersion",
                   "serverSoftware", "pluginVersion", "coreCount", "osArch",
                   "location", "os", "javaVersion"]

def get_stats(spigot_id="",
              bstats_id="",
              bstats_charts=_default_charts):
    http = urllib3.PoolManager()
    """
    Get current plugin statistics from Spigot and/or bStats.
    At least one of spigot_id and bstats_id should be provided,
    and if bstats_id is provided then bstats_charts should contain
    at least one chart.

    Keyword arguments:
    spigot_id -- the Spigot id of the plugin
    bstats_id -- the bStats id of the plugin
    bstats_charts -- list of charts to read from bStats, defaults to all
    """
    spigot_id = spigot_id.strip()
    bstats_id = bstats_id.strip()

    if not spigot_id and not bstats_id:
        warnings.warn("Neither spigot_id or bstats_id set")
    if bstats_id and not bstats_charts:
        warnings.warn("bstats_id set but bstats_charts empty")

    results = {}

    if spigot_id:
        spigot_url = f"https://api.spigotmc.org/simple/0.1/index.php?action=getResource&id={spigot_id}"
        results['spigot'] = _get_json(spigot_url, http)

    if bstats_id:
        results['bstats'] = {}
        bstats_url = f"https://bstats.org/api/v1/plugins/{bstats_id}/charts/"
        for chart in bstats_charts:
            results['bstats'][chart] = _get_bstats_chart(bstats_id, chart, http)

    return results


def _get_bstats_chart(bstats_id, chart, http):
    # Get the chart data from bStats for the given chart and bStats id.
    # In the case of the 'servers' and 'players' chart ?maxElements=1 is
    # added to the request to get only the current count, not the historical
    # values.
    bstats_url = f"https://bstats.org/api/v1/plugins/{bstats_id}/charts/{chart}/data/"
    if chart == 'servers' or chart == 'players':
        bstats_url += '?maxElements=1'
    return _get_json(bstats_url, http)

def _get_json(url, http):
    # GET the url as JSON
    req = http.request('GET', url)
    data = json.loads(req.data.decode('utf8'))
    req.release_conn()
    return data

