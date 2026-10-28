# Modeling Human Activity States Using Hidden Markov Models

ALU Year 3 Trimester 2, Formative 2 assignment (Individual).

A Hidden Markov Model, written from scratch with numpy, that recognises four activities from phone motion sensors: **still**, **standing**, **walking** and **jumping**. The data was recorded with the Sensor Logger app on an Android phone (accelerometer and gyroscope at about 105 Hz).

## Results on unseen data

Tested on 3 separate recordings that were never used for training (161 scored windows).

| Activity | Samples | Sensitivity | Specificity | Accuracy |
|---|---|---|---|---|
| Still | 36 | 1.000 | 1.000 | 1.000 |
| Standing | 49 | 0.939 | 1.000 | 0.981 |
| Walking | 39 | 1.000 | 0.967 | 0.975 |
| Jumping | 37 | 0.973 | 1.000 | 0.994 |

Overall accuracy: **97.5%**.

## Project layout

```
hmm_activity_recognition.ipynb   The full pipeline: cleaning, features, HMM, evaluation
hmm_types.py                     Shared record shapes (TypedDicts) used by the notebook
requirements.txt                 Python packages
data/
  raw/                           Sensor Logger exports, unchanged, one folder per recording
    still/ standing/ walking/ jumping/      Training recordings (one activity each)
    test_01/ test_02/ test_03/              Unseen test sessions (all activities in one take)
  cleaned/
    train/                       52 labelled 10 s clips (13 per activity), resampled to 100 Hz
    test/                        The 3 test sessions, resampled and labelled per row
  test_labels.csv                True activity blocks for each test session
figures/                         Every figure used in the report, saved by the notebook
```

## Pipeline

1. **Clean:** resample every recording onto a fixed 100 Hz grid, trim 2 s from each end, cut into 10 s clips
2. **Features:** 2 s windows with a 1 s step, 6 time-domain and 2 FFT features, log scale and z-score
3. **Train:** Gaussian HMM trained with Baum-Welch, stopping when the log-likelihood improves by less than 1e-4
4. **Decode:** Viterbi on each unseen test session
5. **Evaluate:** sensitivity, specificity, accuracy and a confusion matrix

## How to run

From the project root:

```
pip install -r requirements.txt
jupyter nbconvert --to notebook --execute --inplace hmm_activity_recognition.ipynb
```

Or open `hmm_activity_recognition.ipynb` in VS Code or Jupyter and run every cell from top to bottom.
