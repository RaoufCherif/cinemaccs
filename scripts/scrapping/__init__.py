from dagster import Definitions, load_assets_from_modules, define_asset_job, AssetSelection, ScheduleDefinition
from . import assets


all_assets = load_assets_from_modules([assets])

scrapping_job = define_asset_job("scrapping_job", selection=(AssetSelection.groups("scrapping")))
scrapping_schedule = ScheduleDefinition(
    job=scrapping_job,
    cron_schedule="30 3 * * WED",
)

defs = Definitions(
    assets = all_assets,
    schedules = [scrapping_schedule],
)