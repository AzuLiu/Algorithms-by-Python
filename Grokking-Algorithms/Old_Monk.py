def old_monk(n):
    content = '从前有座山\n山里有座庙\n庙里有个老和尚给小和尚讲故事\n讲的故事是:'
    print(content)
    if n < 1:
        print('......')
    else:
        return old_monk(n-1)


n = int(input('我有很多故事,你想听几个？\n'))
old_monk(n)
