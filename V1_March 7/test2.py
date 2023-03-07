# from numpy import frombuffer, int16
# from pyaudio import PyAudio,paInt16
# from whisper import load_model
# from warnings import filterwarnings

# class STT:
#     def __init__(self):
#         filterwarnings('ignore')
        
#     def myCommand(self, threshold=0.001, max_silence=5): 
#         chunk = 1024 
#         sample_format = paInt16  
#         channels = 1
#         fs = 16000 
#         p = PyAudio()
#         model = load_model("small.en")
#         stream = p.open(format=sample_format,
#                     channels=channels,
#                     rate=fs,
#                     frames_per_buffer=chunk,
#                     input=True)
#         frames = []
#         print("Speak now...")
#         silent_frames = 0
#         while True:
#             data = stream.read(chunk)
#             frames.append(data)
#             audio_data = frombuffer(data, dtype=int16)
#             if audio_data.max() < threshold:
#                 silent_frames += 1
#             # else:
#                 silent_frames = 0
                
#             if silent_frames / (fs / chunk) > max_silence:
#                 break
#             stream.stop_stream()
#             stream.close()
#             print("Recording completed.")
    
#         audio_data = frombuffer(b''.join(frames), dtype=int16)
#         audio_data = audio_data.astype('float32') / 32767.0
#         result = model.transcribe(audio_data)
#         print(result["text"])
#         p.terminate()


        
        
# obj = STT()
# while True:
#     obj.myCommand()
        