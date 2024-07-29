import cv2
class VideoCamera(object):
  def __init__(self,videofile):
    self.cap =cv2.VideoCapture(videofile)
    
    try:
        while (cap.isOpened()):

            ret, frame = cap.read()
            # describe the type of font
            # to be used.
            #font = cv2.FONT_HERSHEY_SIMPLEX
            print(frame)
            #cv2.imshow('video', frame)
            #if cv2.waitKey(1) & 0xFF == ord('q'):
                #break
    except AttributeError:
        return 'NO VIOLENCE DETECTED...'
    cap.release()

    cv2.destroyAllWindows()