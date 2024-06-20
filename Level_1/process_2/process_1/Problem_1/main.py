#"Hello Mars" 출력 (예외 처리 포함)
try:
    print('Hello Mars')
except Exception as e:
    print('ERROR:', e)

#"mission_computer_main.log" 파일을 읽어 화면에 출력 (예외 처리 포함)
try:
    with open('mission_computer_main.log', 'r') as file:
        for line in file:
            print(line.rstrip())
except Exception as e:
    print('ERROR:', e)

#"mission_computer_main.log" 파일을 시간 역순으로 화면에 출력 (예외 처리 포함)
try:
    with open('mission_computer_main.log', 'r') as file:
        lines = file.readlines()
    for line in reversed(lines):
        print(line.rstrip())
except Exception as e:
    print('ERROR:', e)
    
#Markdown 형식 보고서 저장 및 문제가 되는 부분 따로 저장 ("unstable", "explosion", "powered down" 등 포함):
try:
    with open('log_analysis.md', 'w', encoding='utf-8') as report_file, \
         open('문제 발생.txt', 'w', encoding='utf-8') as problematic_logs_file, \
         open('mission_computer_main.log', 'r', encoding='utf-8') as log_file:
         
        for line in log_file:
            timestamp, event, message = line.strip().split(',')
            markdown_line = f'| {timestamp} | {event} | {message} |\n'
            report_file.write(markdown_line)
            
            if 'unstable' in message or 'explosion' in message or 'powered down' in message:
                problematic_logs_file.write(markdown_line)
except Exception as e:
    print('ERROR:', e)
