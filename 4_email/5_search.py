from imap_tools import MailBox, AND, OR, NOT
from account import *


with  MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    # for msg in mailbox.fetch('(UNSEEN)'): # 읽지 않은 메일 가져오기
        # print(f"[{msg.from_}] {msg.subject}")
        
    # 특정인이 보낸 메일 가져오기
    # for msg in mailbox.fetch('(from intaechoi@mz.co.kr)', limit=3, reverse=True): 
        # print(f"[{msg.from_}] {msg.subject}")
    
    # 특정 글자를 포함하는 메일, 제목 + 본문,  ' "dd" ' 구조로 해야됨
    # for msg in mailbox.fetch('(TEXT "test mail")'): 
        # print(f"[{msg.from_}] {msg.subject}")
        
    # 제목만 검색 (한글 검색은 안됨 -> if "검색할 한글" in msg.subject: 처리)
    # for msg in mailbox.fetch('(subject "test mail")'):
    #     print(f"[{msg.from_}] {msg.subject}")
    
    # 특정 날짜 이후의 메일
    # for msg in mailbox.fetch('(sentsince 07-Nov-2020)', limit=5, reverse=False):
        # print(f"[{msg.from_}] {msg.subject}")
        
    # 특정 날짜에 온 메일, or 조건 묶기
    # for msg in mailbox.fetch(OR('ON 11-Nov-2022', 'ON 14-Nov-2022', 'FROM intaechoi@mz.co.kr'), limit=10, reverse=True):
    #     print(f"{msg.date_str} [{msg.from_}] {msg.subject} ")
    
    # 특정 조건
    for msg in mailbox.fetch(
            AND(
                OR(
                    AND('SENTSINCE 17-Nov-2022', 'SENTBEFORE 18-Nov-2022'),
                    AND('SENTSINCE 11-Nov-2022', 'SENTBEFORE 12-Nov-2022'),
                ),
                NOT(from_='no-reply@accounts.google.com'),
                NOT('from intaechoi@mz.co.kr'),
                # 'from admin_workflow@mz.co.kr'
            ),
            limit=10, 
            reverse=True,
        ):
        print(f"{msg.date_str} [{msg.from_}] {msg.subject} ")
        