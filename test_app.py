import unittest

from app import build_payload


class PayloadTest(unittest.TestCase):
    def test_payload_contains_week_one_topics(self):
        payload = build_payload()

        self.assertEqual(payload["message"], "Hello Harness")
        self.assertEqual(payload["week"], 1)
        self.assertIn("git", payload["topics"])
        self.assertIn("docker", payload["topics"])
        self.assertIn("yaml", payload["topics"])


if __name__ == "__main__":
    unittest.main()
