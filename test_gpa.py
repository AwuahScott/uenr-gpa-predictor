import unittest
from gpa_calc import calculate_cgpa, predict_target

class TestGPACalculator(unittest.TestCase):

    def test_calculate_cgpa_valid(self):
        """Test CGPA calculation with regular course data."""
        mock_records = {
            "Sem1": [
                {"course": "INFT 355", "credits": 3, "grade_point": 4.0}, # A
                {"course": "INFT 351", "credits": 2, "grade_point": 2.5}  # C+
            ]
        }
        # Expected: ((3 * 4.0) + (2 * 2.5)) / (3 + 2) = (12 + 5) / 5 = 17 / 5 = 3.4
        cgpa, total_credits = calculate_cgpa(mock_records)
        self.assertEqual(cgpa, 3.4)
        self.assertEqual(total_credits, 5)

    def test_calculate_cgpa_empty(self):
        """Test CGPA calculation when no courses have been added."""
        mock_records = {}
        cgpa, total_credits = calculate_cgpa(mock_records)
        self.assertEqual(cgpa, 0.0)
        self.assertEqual(total_credits, 0)

    def test_predict_target_achievable(self):
        """Test prediction calculation when the goal is realistic."""
        # Current: 20 credits at 3.5 CGPA. Target: 3.6 CGPA. Remaining: 20 credits.
        required_gpa = predict_target(
            current_cgpa=3.5, 
            current_credits=20, 
            target_cgpa=3.6, 
            remaining_credits=20
        )
        self.assertEqual(required_gpa, 3.7)

if __name__ == "__main__":
    unittest.main()
