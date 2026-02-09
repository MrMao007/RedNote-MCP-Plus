from playwright.async_api import async_playwright
import asyncio

from rednote_mcp_plus.read.dump import dumpNote


async def search(keyWord: str, topN: int) -> list[str]:
    """
    搜索小红书笔记
    """
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        context = await browser.new_context(storage_state="src/rednote_mcp_plus/cookie/rednote_cookies.json")
        page = await context.new_page()
        await page.goto("https://www.xiaohongshu.com/search_result?keyword=" + keyWord)
        print("🌐 导航到小红书主页...")
        await page.wait_for_timeout(3000)
        login_button = page.locator("form").get_by_role("button", name="登录")
        if(await login_button.is_visible()):
            return ["❌ 未登录小红书，请先登录"]
        
        herfs = []
        prefix = 'https://www.xiaohongshu.com'
        links = await page.query_selector_all('a.cover.mask.ld')
        # 获取所有 href 属性
        hrefs = []
        for link in links:
            href = await link.get_attribute('href')
            if href:
                href = prefix + href
                hrefs.append(href)
            if len(hrefs) >= topN:
                break
        markdown_content = []
        for href in hrefs:
            hrefs.append


        await browser.close()
        await context.close()
            
        return hrefs
            
        

if __name__ == "__main__":
    result = asyncio.run(search("测试", 5))
    print(result)