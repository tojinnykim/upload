import requests
import dotenv
import os
import zipfile

dotenv.load_dotenv()

key = os.getenv('OPEN_DART_KEY')

if not key:
    print("API 키가 없습니다. .env 파일을 확인하세요.")
    exit()

url = 'https://opendart.fss.or.kr/api/corpCode.xml'
params = {
    'crtfc_key': key,
}

print("API 요청 중...")
response = requests.get(url, params=params)

print(f"응답 코드: {response.status_code}")
print(f"Content-Type: {response.headers.get('content-type', 'Unknown')}")
print(f"응답 크기: {len(response.content)} bytes")

if response.status_code == 200:
    # 응답이 에러 메시지인지 확인
    if response.content.startswith(b'<?xml'):
        print("에러: XML 응답을 받았습니다. API 키를 확인하세요.")
        print(response.text[:200])
    else:
        # zip 파일 저장
        with open('codes.zip', 'wb') as f:
            f.write(response.content)
        print("zip 파일 저장 완료")
        
        # 압축 해제 시도
        try:
            with zipfile.ZipFile('codes.zip', 'r') as zip_ref:
                zip_ref.extractall('.')
            print("압축 해제 성공!")
            
            # 결과 파일 확인
            for file in os.listdir('.'):
                if file.endswith('.xml'):
                    print(f"생성된 파일: {file}")
                    
        except zipfile.BadZipFile:
            print("zip 파일이 손상되었습니다.")
            # 파일 내용 확인
            with open('codes.zip', 'rb') as f:
                content = f.read(100)
                print(f"파일 시작 부분: {content}")
                
else:
    print(f"API 호출 실패: {response.status_code}")
    print(f"오류 내용: {response.text}")