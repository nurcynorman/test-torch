does pytoch have a future?
> ps : in the face of LLMs , is there a point to learn pytoch? is there still value if so where is the value?

* pytorch used to make most of LLMs , it what OpenAI uses.
    * does pytorch dominance in research enough to say OpenAI must have uses it
    * can refer gpt2 , https://github.com/openai/gpt-2, can refer to any from doiscussions
```Dockerfile
FROM tensorflow/tensorflow:1.12.0-py3

ENV LANG=C.UTF-8
RUN mkdir /gpt-2
WORKDIR /gpt-2
ADD . /gpt-2
RUN pip3 install -r requirements.txt
RUN python3 download_model.py 124M
RUN python3 download_model.py 355M
RUN python3 download_model.py 774M
RUN python3 download_model.py 1558M
```
* since gpt use tensorflow and tensorflow's decline in research. they might have swapped to pytorch.
    * tensorflow still widely used in production systems, has lost ground in the research community due to its static computation graph and steeper learning cruve

* but people sometimes combine it together since tensorflow excels in production deployment(Tensorflow Serving, Tensorflow Lite), while PyTorch is more flexible for research and experiment.
* deepspeed by microsoft built on top of pytorch, 

* Pytorch is just a library built on top of python like a framework get down with pip everything will fall in line learning a fork and not the foundations is limiting yourself specially if you gonna work with Jupiter notebooks

music vids : https://www.youtube.com/watch?v=LF7AezBpqzg&ab_channel=limiminami
