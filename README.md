# Data Project 2

Michael He, Anish Jagota

## Setup

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```
http://34.67.73.82:5001/chat?question=<your question>
```

## Examples

### Example 1

If I wanted to know the price of bitcoin and the fear and greed index on April 18 2025, I would use the following URL:

```
http://34.67.73.82:5001/chat?question=what%20is%20the%20price%20of%20bitcoin%20and%20fear%20and%20greed%20index%20on%20April%2018%202025
```

### Example Reponse 1

```json
{
    "response": "Based on the provided data, there is no date listed for April 18, 2025."
}
```

### Example 2

If I wanted to ask Gemini about the months when the fear index was the highest, I would use the following URL:

```

http://34.67.73.82:5001/chat?question=what%20months%20was%20the%20fear%20index%20the%20highest

```

### Example Response 2

```json
{
    "response": "Based on the provided data, here's a breakdown of the months with the highest
	Fear and Greed Index values:\n\nTo accurately get an answer I would need to know what
	\"the highest\" range is to better determine which months were the \"highest.\" \n\nHowever,
	after looking through the data, it appears that the months with the highest fear and greed
	index were February 2021 with an index of 95 and June 2019 with an index of 95, closely
	followed by other months with an index ranging from 80-90."
}
```

### [Reflection PDF](https://github.com/MichaelHeUVA/Data-Project-2/blob/main/Reflection%20Report.pdf)
