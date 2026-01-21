import json
import re
from playwright.async_api import async_playwright
import asyncio
from datetime import datetime

async def dumpUser(userUrl: str) -> str:
    """
    导出小红书用户信息
    :param userUrl: 用户主页URL
    """
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context(storage_state="src/rednote_mcp_plus/cookie/rednote_cookies.json")
        page = await context.new_page()
        await page.goto(userUrl)
        print("🌐 导航到小红书用户主页...")
        await page.wait_for_timeout(1000)
        login_button = page.locator("form").get_by_role("button", name="登录")
        if(await login_button.is_visible()):
            return "❌ 未登录小红书，请先登录"
        
        # 获取 HTML 内容
        html = await page.content()

        # 正则提取 JSON 字符串
        match = re.search(
            r'window\.__INITIAL_STATE__\s*=\s*({.*?})(?=</script>)', 
            html, 
            re.DOTALL
        )

        if match:
            json_str = match.group(1)
            data = json.loads(json_str)
            print(data['user'])

        try:
            # 无限等待，直到页面被关闭
            await page.wait_for_event("close", timeout=0)
        except Exception as e:
            print(f"等待过程中断: {e}")
        finally:
            await context.close()
            await browser.close()
            
        return html
    
if __name__ == "__main__":
    url='https://www.xiaohongshu.com/user/profile/63d944e20000000026012158?xsec_token=AB9u7T-ZtG7Qt-PFS7HbIfqFCZcnXEUI4baNtc9ac9de4=&xsec_source=pc_note'
    result = asyncio.run(dumpUser(url))