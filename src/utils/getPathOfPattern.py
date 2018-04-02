import os

def getPathOfPattern(patternName):
    # popen 用于将shell执行结果返回
    opencvPath = os.popen(
        'brew info opencv | grep "\/usr\/[^\d]*" | cut -d " " -f 1').read(
        ).strip()
    # 识别模式文件路径
    patternPath = os.popen(
        'find ' + opencvPath + ' -name "' + patternName + '"').read()
    return patternPath.strip()
