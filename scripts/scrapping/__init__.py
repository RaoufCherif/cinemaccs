from dagster import (
    AssetSelection,
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_modules,
)

from . import assets

all_assets = load_assets_from_modules([assets])

scrapping_job = define_asset_job(
    "scrapping_job", selection=(AssetSelection.groups("scrapping"))
)
scrapping_schedule = ScheduleDefinition(
    job=scrapping_job,
    cron_schedule="30 3 * * WED",
)

defs = Definitions(
    assets=all_assets,
    schedules=[scrapping_schedule],
)
