# EEG-LOC-Game-analysis-project

The present project tries to extend prior work on the AffPac dataset beyond binary BCI classifier comparisons toward a full multimodal neurophysiological characterization of the LOC state. Specifically, the six analysis modules address the following objectives:

•	Project 1: Quantify central cortical rhythm modulation (ERD/ERS) and peripheral autonomic arousal (GSR, respiration, plethysmography) during normal versus LOC conditions.

•	Project 2: Identify and characterize Error-Related Potentials (ErrPs / ERN) at fronto-central electrodes using stimulus-locked grand average waveforms across the cohort.

•	Project 3: Measure beta-band corticomuscular coherence between C3 & C4 (EEG) and forearm EMG as a function of LOC-induced attentional modulation.

•	Project 4: Compute Phase-Locking Values between fronto-central (FC2) and motor cortex (C4) electrodes to detect LOC-induced functional network reorganization.

•	Project 5: Extract and statistically compare frontal midline theta (4-8 Hz) power at FC1/FC2 as a cognitive conflict alarm marker.

•	Project 6: Compute and compare Frontal Alpha Asymmetry (FAA) indices to track the affective frustration and approach-withdrawal dynamics induced by LOC.


The dataset analyzed in this study is the Affective Pacman (AffPac) dataset, publicly available through the BNCI Horizon 2020 research database (bnci-horizon-2020.eu/database/data-sets). It was originally collected and described by Reuderink and is associated with the empirical study published in Reuderink et al. (2011). The original purpose was to investigate the effect of user mental state specifically frustration arising from loss of motor control on the reliability of movement-based BCI classifiers. The dataset is openly licensed for academic research and distributed as per-subject MATLAB (.mat) archive files, each downloadable individually.

Twelve healthy adult participants (S00 through S11) were originally recorded. Subjects S03 and S08 declined to release their data for public distribution and were excluded from the anonymized dataset. The current analysis therefore utilized the remaining N = 10 subjects (S00, S01, S02, S04, S05, S06, S07, S09, S10, S11). All subjects had normal or corrected-to-normal vision, reported no medication use at the time of recording, and were predominantly right-handed. Most had some prior video game experience; four had previous experience with BCI systems (Reuderink et al., 2011).

Participants played a custom variant of the classic Pacman arcade game. Control was simplified to two buttons: a left index-finger button turned the Pacman avatar 90° counterclockwise, while a right index-finger button turned it 90° clockwise. Experimental sessions followed an interleaved block design where LOC was induced in one-third of randomized two-minute blocks. In LOC blocks, 15% of key strokes were silently ignored by the game engine, and an additional visual display lag was introduced. Normal blocks remained unmodified. After each two-minute block, participants rated their emotional state using the Self-Assessment Manikin (SAM; Bradley & Lang, 1994) on three 9-point Likert scales: valence (unpleasant-pleasant), arousal (calm-excited), and dominance (controlled-in control). The total session duration was approximately 30 minutes (Reuderink et al., 2011; Reuderink, 2014).



A BioSemi ActiveTwo EEG system recorded all signals simultaneously at 512 Hz sampling rate with 32 active Ag/AgCl EEG electrodes placed in the extended 10–20 system layout. 
