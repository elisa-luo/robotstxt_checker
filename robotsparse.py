import subprocess

ROBOTS_PARSER_PATH = "bazel-bin/robots_main"

def check_bot_access(robots_txt_path, botname, full_url):
    """
    Args:
    robots_txt_path (str): Path to the robots.txt file.
    botname (str): The name of the bot (e.g., 'Googlebot').
    full_url (str): The full URL that the bot wants to access.
    
    Returns:
    bool: True if the bot is allowed, False otherwise.
    """
    
    try:
        # Run the command using subprocess
        command = ['./' + ROBOTS_PARSER_PATH, robots_txt_path, botname, full_url]
        result = subprocess.run(command, capture_output=True, text=True)
        # output = result.stdout
        code = result.returncode
        # print(code, output)
        
        # check the return code for the results
        if code == 0:
            return True  # bot is allowed
        elif code == 1:
            return False  # bot is disallowed
        return None  # error parsing robots.txt

    except subprocess.CalledProcessError as e:
        print(f"Error running the command: {e}")
        return False
    
# enumerate all paths provided in robots.txt
def get_all_paths_from_robots(robots_content):
    all_paths = set()
    for line in robots_content:
        if "Disallow: " in line or "Allow: " in line:
            all_paths.add(line.split()[1])
    return list(all_paths)

'''
    for each path, check if the given useragent is disallowed from it.
    if for all paths in robots.txt the useragent is disallowed
    then this means the user agent is complete disallowed.
    return True if the useragent is completely disallowed
'''
def check_completely_disallowed(all_paths, useragent, robots_path, url):
    if url[-1] == '/': # remove trailing slash
        url = url[:-1]
    for path in all_paths:
        full_path = url + path
        if check_bot_access(robots_path, useragent, full_path):  # bot is allowed for this path
            # print("looks like {} is allowed to access {}".format(useragent, full_path))
            return False
    return True # if all paths are disallowed


# Examples
with open("nba_robots.txt", "r") as file:
    content = file.readlines()
    # print(get_all_paths_from_robots(content))
    print(check_completely_disallowed(get_all_paths_from_robots(content), 'GPTBot', "nba_robots.txt", "https://nba.com/"))

print(check_bot_access("nba_robots.txt", "GPTBot", "https://nba.com/"))