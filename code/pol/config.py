import pol.utils as utils
import pol.info as info

work_outlier_agents = info.work_outlier_agents
work_outlier_map = utils.get_outlier_map(work_outlier_agents, 'WORK')

social_outlier_agents = info.social_outlier_agents
social_outlier_map = utils.get_outlier_map(social_outlier_agents, 'SOCIAL')

hunger_outlier_agents = info.hunger_outlier_agents
hunger_outlier_map = utils.get_outlier_map(hunger_outlier_agents, 'HUNGER')

combined_outlier_agents = info.combined_outlier_agents
combined_work_outlier_agents = combined_outlier_agents['WORK']
combined_work_outlier_map = utils.get_outlier_map(
    combined_work_outlier_agents, 'WORK')

combined_social_outlier_agents = combined_outlier_agents['SOCIAL']
combined_social_outlier_map = utils.get_outlier_map(
    combined_social_outlier_agents, 'SOCIAL')

combined_hunger_outlier_agents = combined_outlier_agents['HUNGER']
combined_hunger_outlier_map = utils.get_outlier_map(
    combined_hunger_outlier_agents, 'HUNGER')

# integrated outlier maps in one map
combined_outlier_map = {}
combined_outlier_map.update(combined_work_outlier_map)
combined_outlier_map.update(combined_social_outlier_map)
combined_outlier_map.update(combined_hunger_outlier_map)


maps = {
    'work-outliers': work_outlier_map,
    'hunger-outliers': hunger_outlier_map,
    'social-outliers': social_outlier_map,
    'combined-outliers': combined_outlier_map
}
