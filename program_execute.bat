pyinstaller --onedir -w --add-data "forms/purrfectmatch_frame/*.png;forms/purrfectmatch_frame" --add-data  "data/*.csv;data" --add-data "data/*.txt;data" purrfectmatch.py

pyinstaller --onedir -w --add-data "forms/adoption1_frame/*.png;forms/adoption1_frame" adoptframe1.py -y

pyinstaller --onedir -w --add-data "forms/adoption2_frame/*.png;forms/adoption2_frame" adoptframe2.py -y

pyinstaller --onedir -w --add-data "forms/adoption3_frame/*.png;forms/adoption3_frame" adoptframe3.py -y

pyinstaller --onedir -w --add-data "forms/adoption4_frame/*.png;forms/adoption4_frame" adoptframe4.py -y

pyinstaller --onedir -w --add-data "forms/adoption5_frame/*.png;forms/adoption5_frame" adoptframe5.py -y

pyinstaller --onedir -w --add-data "forms/adoption6_frame/*.png;forms/adoption6_frame" adoptframe6.py -y

pyinstaller --onedir -w --add-data "forms/donate_frame/*.png;forms/donate_frame" donateframe.py -y

pyinstaller --onedir -w --add-data "forms/favorites1_frame/*.png;forms/favorites1_frame" favoritesframe.py -y

pyinstaller --onedir -w --add-data "forms/feedback_frame/*.png;forms/feedback_frame" feedbackframe.py -y

pyinstaller --onedir -w --add-data "forms/forgetpass_frame/*.png;forms/forgetpass_frame" forgetpassframe1.py -y

pyinstaller --onedir -w --add-data "forms/home_frame/*.png;forms/home_frame" --add-data "forms/home_frame/cats/candy/*.png;forms/home_frame/cats/candy" --add-data "forms/home_frame/cats/lemon/*.png;forms/home_frame/cats/lemon" --add-data "forms/home_frame/cats/luna/*.png;forms/home_frame/cats/luna" --add-data "forms/home_frame/cats/orange/*.png;forms/home_frame/cats/orange" --add-data "forms/home_frame/cats/sugar/*.png;forms/home_frame/cats/sugar" --add-data "forms/home_frame/dogs/fiona/*.png;forms/home_frame/dogs/fiona" --add-data "forms/home_frame/dogs/kaira/*.png;forms/home_frame/dogs/kaira" --add-data "forms/home_frame/dogs/levis/*.png;forms/home_frame/dogs/levis" --add-data "forms/home_frame/dogs/milo/*.png;forms/home_frame/dogs/milo" --add-data "forms/home_frame/dogs/pepper/*.png;forms/home_frame/dogs/pepper" homeframe.py -y

pyinstaller --onedir -w --add-data "forms/privacy1_frame/*.png;forms/privacy1_frame" privacyframe1.py -y

pyinstaller --onedir -w --add-data "forms/privacy2_frame/*.png;forms/privacy2_frame" privacyframe2.py -y

pyinstaller --onedir -w --add-data "forms/privacy3_frame/*.png;forms/privacy3_frame" privacyframe3.py -y

pyinstaller --onedir -w --add-data "forms/register_frame/*.png;forms/register_frame" registerframe.py -y

pyinstaller --onedir -w --add-data "forms/signup1_frame/*.png;forms/signup1_frame" signupframe1.py -y

pyinstaller --onedir -w --add-data "forms/signup2_frame/*.png;forms/signup2_frame" signupframe2.py -y

pyinstaller --onedir -w --add-data "forms/terms1_frame/*.png;forms/terms1_frame" termsframe1.py -y

pyinstaller --onedir -w --add-data "forms/terms2_frame/*.png;forms/terms2_frame" termsframe2.py -y

pyinstaller --onedir -w --add-data "forms/thankyou_adopt/*.png;forms/thankyou_adopt" thankyou_adopt.py -y

pyinstaller --onedir -w --add-data "forms/thankyou_donate/*.png;forms/thankyou_donate" thankyou_donate.py -y

pyinstaller --onedir -w --add-data "forms/thankyou_signup/*.png;forms/thankyou_signup" thankyou_signup.py -y