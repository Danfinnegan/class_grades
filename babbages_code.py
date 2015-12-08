def statistics(grades):
    import numpy as np
    
    mean = np.mean(grades)
    std = np.std(grades)
    high = np.max(grades)
    low = np.min(grades)

    return mean,std,high,low
