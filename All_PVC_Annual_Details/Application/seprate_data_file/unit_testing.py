# import unittest
# from unittest.mock import patch, MagicMock
# from io import StringIO
# # from seprate_file_backend import main
# from seprate_file_backend import main

# class TestMainFunction(unittest.TestCase):
#     @patch('seprate_file_backend.speak')
#     @patch('seprate_file_backend.answer_question')
#     def test_main_with_valid_question(self, mock_answer_question, mock_speak):
#         # Mock the user input
#         with patch('builtins.input', return_value='What is the revenue of Astral?'):
#             # Mock the return values for the mocked functions
#             mock_answer_question.return_value = 'The revenue of Astral is $1 million.'

#             # Capture the output
#             output = StringIO()
#             with patch('sys.stdout', new=output):
#                 # Call the main function
#                 main()

#             # Assertions
#             self.assertEqual(output.getvalue().strip(), 'Question: What is the revenue of Astral?\nAnswer: The revenue of Astral is $1 million.')
#             mock_speak.assert_any_call('Question: What is the revenue of Astral?')
#             mock_speak.assert_any_call('The revenue of Astral is $1 million.')

#     @patch('seprate_file_backend.speak')
#     @patch('seprate_file_backend.recognize_speech')
#     def test_main_with_audio_error(self, mock_recognize_speech, mock_speak):
#         # Mock the user input
#         with patch('builtins.input', return_value='Could not understand audio, Please try speaking again'):
#             # Mock the return value for the mocked function
#             mock_recognize_speech.return_value = 'Could not understand audio, Please try speaking again'

#             # Capture the output
#             output = StringIO()
#             with patch('sys.stdout', new=output):
#                 # Call the main function
#                 main()

#             # Assertions
#             self.assertEqual(output.getvalue().strip(), 'Question: Could not understand audio, Please try speaking again\nAnswer: Please try speaking again')
#             mock_speak.assert_called_once_with('Could not understand audio, Please try speaking again')

# if __name__ == '__main__':
#     unittest.main()
    
    
    
import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import sys

# Import the function you want to test from the module
from seprate_file_backend import main

class TestMainFunction(unittest.TestCase):
    @patch('seprate_file_backend.speak')
    @patch('seprate_file_backend.answer_question')
    def test_main_with_valid_question(self, mock_answer_question, mock_speak):
        # Mock the user input
        with patch('builtins.input', return_value='What is the revenue of Astral?'):
            # Mock the return values for the mocked functions
            mock_answer_question.return_value = 'The revenue of Astral is $1 million.'

            # Capture the output
            output = StringIO()
            sys.stdout = output

            # Call the main function
            main()

            # Reset the standard output
            sys.stdout = sys.__stdout__

            # Assertions
            self.assertEqual(output.getvalue().strip(), 'Question: What is the revenue of Astral?\nAnswer: The revenue of Astral is $1 million.')
            mock_speak.assert_any_call('Question: What is the revenue of Astral?')
            mock_speak.assert_any_call('The revenue of Astral is $1 million.')

    @patch('seprate_file_backend.speak')
    @patch('seprate_file_backend.recognize_speech')
    def test_main_with_audio_error(self, mock_recognize_speech, mock_speak):
        # Mock the user input
        with patch('builtins.input', return_value='Could not understand audio, Please try speaking again'):
            # Mock the return value for the mocked function
            mock_recognize_speech.return_value = 'Could not understand audio, Please try speaking again'

            # Capture the output
            output = StringIO()
            sys.stdout = output

            # Call the main function
            main()

            # Reset the standard output
            sys.stdout = sys.__stdout__

            # Assertions
            self.assertEqual(output.getvalue().strip(), 'Question: Could not understand audio, Please try speaking again\nAnswer: Please try speaking again')
            mock_speak.assert_called_once_with('Could not understand audio, Please try speaking again')

if __name__ == '__main__':
    unittest.main()
    
    