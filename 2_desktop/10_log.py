from datetime import datetime
import logging

# # format: 시간 정보 [로그레벨] 메세지
# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")
# # debug < info < warning < error < critical
# logging.debug("뭐고 이게")
# logging.info("수행 줁비")
# logging.warning("경고 경고!!")
# logging.error("에러가 발생했습니다")
# logging.critical("심각한 문제 발생")


# 파일에 로그 남기기
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logFormatter = logging.Formatter("%(asctime)s ㅋ [%(levelname)s] %(message)s")

# 스트림 (터미널)
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler) # 스트림에 로그가 나오게 됨

filename = datetime.now().strftime("logs/mylogfile_%Y%m%d %H%M%S.log")
# 파일
fileHandler = logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.debug("로그를 남기는 테스트중")