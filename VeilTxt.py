import wave
import argparse
import numpy


def parseArgs():
    argParser = argparse.ArgumentParser()
    argParser.add_argument("--veil", action='store_true', help='Hide a text message within an audio file...')
    argParser.add_argument("--unveil", action='store_true', help='Read a text message hidden within an audio file...')
    argParser.add_argument("--wav", type=str, help="Path to the .wav audio file to read.")
    argParser.add_argument("--swave", type=str, help="Path to save the encoded .wav file")
    argParser.add_argument("--message", type=str, help="Text message to bind to the .wav file")
    return argParser.parse_args()


def outError(msg):
    print("[ERROR] :   " + msg)


def veilTxt(cmdLine):
    if cmdLine.wav is None or cmdLine.swave is None or cmdLine.message is None:
        outError("Please provide the required arguments needed for veiling a text message...")
        return

    # try:
    wavHandle = wave.open(cmdLine.wav, mode='rb')
    outWav = wave.open(cmdLine.swave, mode='wb')
    frmCount = wavHandle.getnframes()
    if frmCount < 300:
        outError("Please provide a larger enough audio file to continue with the operation...")
        return

    if len(cmdLine.message) > 255 or len(cmdLine.message) < 20:
        outError(
            "Message length cannot exceed the maximum allowed character limit of 255 and cannot subceed the minimum allowed character limit of 50...")
        return

    frmBytes = bytearray(wavHandle.readframes(frmCount))
    xorByte = frmBytes[0]
    frmBytes[1] = len(cmdLine.message)
    for charPos in range(2, len(cmdLine.message) + 2):
        frmBytes[charPos] = xorByte ^ ord(cmdLine.message[charPos - 2])

    outWav.setparams(wavHandle.getparams())
    outWav.setnchannels(wavHandle.getnchannels())
    outWav.writeframes(bytes(frmBytes))
    outWav.close()
    wavHandle.close()
    # except Exception as e:


def unveilTxt(cmdLine):
    if cmdLine.wav is None:
        outError("Please provide the required arguments needed for unveiling the hidden text message...")
        return

    wavHandle = wave.open(cmdLine.wav, mode='rb')
    frmCount = wavHandle.getnframes()
    frmBytes = bytearray(wavHandle.readframes(frmCount))
    xorByte = frmBytes[0]
    msgLen = frmBytes[1]
    msgStr = ""
    for frmIndex in range(2, msgLen + 2):
        msgStr += chr(xorByte ^ frmBytes[frmIndex])

    print("Hidden Text : " + msgStr)


if __name__ == "__main__":
    cmdParams = parseArgs()
    #print(cmdParams)
    if cmdParams.veil:
        veilTxt(cmdParams)
    elif cmdParams.unveil:
        unveilTxt(cmdParams)
    else:
        outError("Provided arguments are invalid...")
