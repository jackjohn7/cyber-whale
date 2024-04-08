from dataclasses import dataclass

@dataclass
class Chat:
    timestamp: int # milliseconds
    content: str # most likely irrelevant but storing in case

def to_cov_bin(data: list[Chat], zero: float, one: float) -> str:
    
    diffs = [] * len(data)
    i, j = 0, 1
    while j < len(data):
        diffs[i] = data[j].timestamp - data[i].timestamp
        i, j += 1

    return "".join(list(map(translate(zero, one), diffs)))

def analyze(data: list[Chat]) -> tuple[float, float]:
    """
    Use statistics to figure out likely 0 and 1 delays
    """
    return (0.0,0.0)

# TODO: Look into whether or not zero is required
# Perhaps it's still needed since you could also 
# calculate based on which the difference is closer to
# or you might also need it when denoising
def translate(zero: float, one: float):
    def aux(diff: float):
        if diff >= one:
            return "1"
        else:
            return "0"

    return aux

def denoise(diffs: list[float]) -> diffs[float]:
    """
    use statistics to denoise data
    """
    # TODO: Implement
    return diffs
