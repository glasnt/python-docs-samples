# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def generate_content(PROJECT_ID: str, REGION: str, MODEL_ID: str) -> object:
    # [START generativeaionvertexai_stream_text_basic]
    import vertexai

    from vertexai.generative_models import GenerativeModel

    vertexai.init(project=PROJECT_ID, location=REGION)

    model = GenerativeModel(MODEL_ID)
    responses = model.generate_content(
        "Write a story about a magic backpack.", stream=True
    )

    for response in responses:
        print(response)
    # [END generativeaionvertexai_stream_text_basic]

    return responses