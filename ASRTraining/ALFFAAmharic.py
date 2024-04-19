"""ALFFAAmharic automatic speech recognition dataset."""


import os
from pathlib import Path

import datasets
from datasets.tasks import AutomaticSpeechRecognition


_CITATION = """\
@inproceedings{
  title={ALFFAAmharic Acoustic-Phonetic Continuous Speech Corpus},
  author={Samuael et al},
}
"""

_DESCRIPTION = """\
The ALFFAAmharic corpus of reading speech has been developed to provide speech data for acoustic-phonetic research studies
and for the evaluation of automatic speech recognition systems.
"""


class ALFFAAmharicASRConfig(datasets.BuilderConfig):
    """BuilderConfig for ALFFAAmharicASR."""

    def __init__(self, **kwargs):
        """
        Args:
          data_dir: `string`, the path to the folder containing the files in the
            downloaded .tar
          citation: `string`, citation for the data set
          url: `string`, url for information about the data set
          **kwargs: keyword arguments forwarded to super.
        """
        super(ALFFAAmharicASRConfig, self).__init__(version=datasets.Version("2.0.1", ""), **kwargs)


class ALFFAAmharic(datasets.GeneratorBasedBuilder):
    """ALFFAAmharicASR dataset."""

    BUILDER_CONFIGS = [ALFFAAmharicASRConfig(name="clean", description="'Clean' speech.")]

    @property
    def manual_download_instructions(self):
        return (
            "To use ALFFAAmharic you have to download it manually. "
            "`datasets.load_dataset('ALFFAAmharic_asr', data_dir='path/to/folder/folder_name')`"
        )

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "file": datasets.Value("string"),
                    "audio": datasets.Audio(sampling_rate=16_000),
                    "text": datasets.Value("string"),
                }
            ),
            supervised_keys=("file", "text"),
            citation=_CITATION,
            task_templates=[AutomaticSpeechRecognition()],
        )

    def _split_generators(self, dl_manager):

        data_dir = os.path.abspath(os.path.expanduser(dl_manager.manual_dir))

        if not os.path.exists(data_dir):
            raise FileNotFoundError(
                f"{data_dir} does not exist. Make sure you insert a manual dir via `datasets.load_dataset('ALFFAAmharic_asr', data_dir=...)` that includes files unzipped from the ALFFAAmharic zip. Manual download instructions: {self.manual_download_instructions}"
            )

        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"split": "train", "data_dir": data_dir}),
            datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={"split": "test", "data_dir": data_dir}),
        ]

    def _generate_examples(self, split, data_dir):
        """Generate examples from ALFFAAmharic archive_path based on the test/train csv information."""
        file = open(f"{data_dir}/{split}/text.txt", "r", encoding="utf-8")
        lines = file.readlines()
        file.close()
        # Iterating the contents of the data to extract the relevant information
        
        for i in range(len(lines)):
            splited = lines[i].strip("\n").split(" ")
            if len(splited)==0:
                continue
            wav_path = f"{data_dir}/{split}/wav/{splited[0]}.wav"
            transcript = " ".join(splited[1:])
            
            yield i, {
                "file": str(wav_path),
                "audio": str(wav_path),
                "text": transcript,
            }


def with_case_insensitive_suffix(path: Path, suffix: str):
    path = path.with_suffix(suffix.lower())
    path = path if path.exists() else path.with_suffix(suffix.upper())
    return path
