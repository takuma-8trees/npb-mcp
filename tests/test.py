from tracker.client import OkaHiromiTracker

def main():
    tracker = OkaHiromiTracker()

    print("=== プロフィール ===")
    profile = tracker.get_profile()
    print(profile)

    print("\n=== 通算打撃成績（キャリア） ===")
    career_stats = tracker.get_career_hitting_stats()
    print(career_stats)

    print("\n=== 2023年シーズン打撃成績 ===")
    season_stats = tracker.get_season_hitting_stats(year=2023)
    print(season_stats)

    print("\n=== 2023年 月別打撃成績 ===")
    monthly_stats = tracker.get_monthly_hitting_stats(year=2023)
    print(monthly_stats)

    print("\n=== 2022年 試合別打撃成績 ===")
    game_stats = tracker.get_game_by_game_hitting_stats(year=2022)
    print(game_stats)

if __name__ == "__main__":
    main()

