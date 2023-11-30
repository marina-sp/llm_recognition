from backend.detection.app.models.detect import create_full_prompt


def test_prompt_creation():
    # Sample test function. Test if the prompt is correctly preprocessed.
    text = "Is this generated with AI?"
    prompt = create_full_prompt(text)

    with open("expected_prompt.txt") as fp:
        expected_prompt = fp.read()

    assert prompt == expected_prompt
