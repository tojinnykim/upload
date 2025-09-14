# 회사 조직도 및 직원 정보를 담은 중첩 딕셔너리
company_data = {
    "개발부": {
        "dept_info": {
            "dept_code": "DEV001",
            "manager": "김개발",
            "location": "서울 강남",
            "budget": 500000000
        },
        "employees": {
            "DEV101": {
                "personal_info": {
                    "name": "이코딩",
                    "age": 28,
                    "position": "선임 개발자",
                    "email": "coding@company.com",
                    "phone": "010-1234-5678"
                },
                "project_history": [
                    {
                        "project_name": "AI 챗봇 개발",
                        "role": "백엔드 개발자",
                        "period": "2024.01 - 2024.06",
                        "skills": ["Python", "Django", "AWS"],
                        "performance_rating": 4.5
                    },
                    {
                        "project_name": "데이터 분석 플랫폼",
                        "role": "풀스택 개발자",
                        "period": "2023.07 - 2023.12",
                        "skills": ["React", "Node.js", "MongoDB"],
                        "performance_rating": 4.8
                    }
                ],
                "salary_history": {
                    "2023": {
                        "base": 45000000,
                        "bonus": 5000000,
                        "stock_options": 2000000
                    },
                    "2024": {
                        "base": 48000000,
                        "bonus": 6000000,
                        "stock_options": 3000000
                    }
                }
            },
            "DEV102": {
                "personal_info": {
                    "name": "박알고",
                    "age": 31,
                    "position": "수석 개발자",
                    "email": "algo@company.com",
                    "phone": "010-2345-6789"
                },
                "project_history": [
                    {
                        "project_name": "블록체인 플랫폼",
                        "role": "리드 개발자",
                        "period": "2024.03 - 2024.09",
                        "skills": ["Solidity", "Web3.js", "Ethereum"],
                        "performance_rating": 4.9
                    }
                ],
                "salary_history": {
                    "2023": {
                        "base": 55000000,
                        "bonus": 8000000,
                        "stock_options": 5000000
                    },
                    "2024": {
                        "base": 60000000,
                        "bonus": 10000000,
                        "stock_options": 7000000
                    }
                }
            }
        }
    },
    "마케팅부": {
        "dept_info": {
            "dept_code": "MKT001",
            "manager": "최마케팅",
            "location": "서울 서초",
            "budget": 300000000
        },
        "employees": {
            "MKT101": {
                "personal_info": {
                    "name": "정브랜드",
                    "age": 29,
                    "position": "브랜드 매니저",
                    "email": "brand@company.com",
                    "phone": "010-3456-7890"
                },
                "project_history": [
                    {
                        "project_name": "브랜드 리뉴얼",
                        "role": "프로젝트 매니저",
                        "period": "2024.01 - 2024.03",
                        "campaigns": ["SNS", "TV광고", "옥외광고"],
                        "performance_rating": 4.7
                    }
                ],
                "salary_history": {
                    "2023": {
                        "base": 42000000,
                        "bonus": 4000000,
                        "performance_incentive": 3000000
                    },
                    "2024": {
                        "base": 45000000,
                        "bonus": 5000000,
                        "performance_incentive": 4000000
                    }
                }
            }
        }
    }
}

# 데이터 접근 예시
print("=== 개발부 정보 ===")
print(f"부서장: {company_data['개발부']['dept_info']['manager']}")
print(f"부서 예산: {company_data['개발부']['dept_info']['budget']:,}원")

print("\n=== 이코딩 프로젝트 이력 ===")
for project in company_data['개발부']['employees']['DEV101']['project_history']:
    print(f"프로젝트명: {project['project_name']}")
    print(f"역할: {project['role']}")
    print(f"기간: {project['period']}")
    print(f"평가점수: {project['performance_rating']}")
    print()

print("=== 박알고 2024년 급여 정보 ===")
salary_2024 = company_data['개발부']['employees']['DEV102']['salary_history']['2024']
total_compensation = salary_2024['base'] + salary_2024['bonus'] + salary_2024['stock_options']
print(f"총 연봉: {total_compensation:,}원")