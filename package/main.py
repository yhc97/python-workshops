from file_finder import find_image_files
from steps import preprocessing, step1, step2, finalstep
from loguru import logger
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


if __name__ == "__main__":

    preprocessing()

    step1()

    step2()

    find_image_files()

    x = np.linspace(0, 1000, 10000)
    test_df = pd.DataFrame(index=x)

    test_df["log_x"] = np.log(x)
    test_df["sin_x"] = np.sin(x)
    test_df["cos_x"] = np.cos(x)

    logger.debug("creating plots")

    fig, ax = plt.subplots(nrows=3, ncols=1)

    plot_idx = 0  # this is for easier rearrangement of order of subplots

    ax[plot_idx].plot(test_df.index, test_df["log_x"])
    plot_idx += 1

    ax[plot_idx].plot(test_df.index, test_df["sin_x"])
    plot_idx += 1

    ax[plot_idx].plot(test_df.index, test_df["cos_x"])
    plot_idx += 1

    if not os.path.isdir("output"):
        os.makedirs("output")
    output_path = os.path.join("output", "test_output.png")

    fig.savefig(output_path)

    logger.info(f"saved image to {output_path}")

    plt.close()

    finalstep()
