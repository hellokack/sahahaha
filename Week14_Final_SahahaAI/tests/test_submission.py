import os
import unittest

os.environ.setdefault("SECRET_KEY", "test-secret")

from app import get_health_payload
from chatbot.dept_directory import STAFF_DIRECTORY_PAGE_URL, search_staff_directory


class SubmissionSmokeTests(unittest.TestCase):
    def test_health_payload(self):
        payload = get_health_payload()
        self.assertEqual(payload["status"], "ok")
        self.assertEqual(payload["service"], "sahaha-ai")
        self.assertEqual(payload["version"], "1.0.0")

    def test_ai_staff_lookup_uses_official_directory_phone(self):
        results = search_staff_directory("사하구청 AI 담당 부서 알려줘", limit=1)
        self.assertTrue(results)

        best = results[0]
        self.assertEqual(best["title"], "AI행정혁신계장")
        self.assertEqual(best["contact"], "051-220-0133")
        self.assertEqual(best["url"], STAFF_DIRECTORY_PAGE_URL)


if __name__ == "__main__":
    unittest.main()
