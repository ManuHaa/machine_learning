from helpers import get_dataframe_from_csv


### --- LOADING DATA --- ###

# player power ranks
player_powerrank_data_filepath = 'csv_files/power_ranks/FIFA23_official_data.csv'
player_powerrank_target_cols = ['Name', 'Age', 'Nationality', 'Overall', 'Club', 'Value', 'Wage']
player_powerrank_dataframe = get_dataframe_from_csv(player_powerrank_data_filepath, player_powerrank_target_cols)

# global team power ranks
golbal_teams_powerrank_data_filepath = 'csv_files/power_ranks/spi_global_rankings.csv'
global_teams_powerrank_dataframe = get_dataframe_from_csv(golbal_teams_powerrank_data_filepath, '')

# league matches
matches_target_cols = ['COUNTRY', 'HOME_TEAM', 'AWAY_TEAM', 'FTR']

## premier league
pem_matches_filepath = 'csv_files/top_5_leagues_match_results/england-premier-league-2022-2023.csv'
pem_matches_dataframe = get_dataframe_from_csv(pem_matches_filepath, matches_target_cols)

## ligue 1
ligue1_matches_filepath = 'csv_files/top_5_leagues_match_results/france-ligue-1-2022-2023.csv'
ligue1_matches_dataframe = get_dataframe_from_csv(ligue1_matches_filepath, matches_target_cols)

## bundesliga
buli_matches_filepath = 'csv_files/top_5_leagues_match_results/germany-bundesliga-2022-2023.csv'
buli_matches_dataframe = get_dataframe_from_csv(buli_matches_filepath, matches_target_cols)

## serie a
seriea_matches_filepath = 'csv_files/top_5_leagues_match_results/italy-serie-a-2022-2023.csv'
seriea_matches_dataframe = get_dataframe_from_csv(seriea_matches_filepath, matches_target_cols)

## laliga
laliga_matches_filepath = 'csv_files/top_5_leagues_match_results/spain-la-liga-2022-2023.csv'
laliga_buli_matches_dataframe = get_dataframe_from_csv(laliga_matches_filepath, matches_target_cols)

# cl matches
cl_data_filepath = 'csv_files/cl/europe-champions-league-2022-2023.csv'
cl_data_target_cols = ['HOME_TEAM', 'AWAY_TEAM', 'FTHG', 'FTAG']
cl_dataframe = get_dataframe_from_csv(cl_data_filepath, cl_data_target_cols)

# uel matches
uel_data_filepath = 'csv_files/uel/europe-europa-league-2022-2023.csv'
uel_data_target_cols = ['HOME_TEAM', 'AWAY_TEAM', 'FTHG', 'FTAG']
uel_data_frame = get_dataframe_from_csv(uel_data_filepath, uel_data_target_cols)


### for testing
#print(cl_dataframe.shape)
#for col in cl_dataframe:
#    print(col)