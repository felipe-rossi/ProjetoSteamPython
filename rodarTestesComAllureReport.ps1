python -m pytest tests/test_steam.py --alluredir=allure-results

allure generate allure-results --clean -o allure-report

allure open allure-report