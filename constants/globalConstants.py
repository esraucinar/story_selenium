#chatbot
BASE_URL="https://tobeto.com"
ANASAYFA_IFRAME="//*[@id='exw-launcher-frame']"
CHATBOT_IFRAME="//*[@id='launcher']/div"
CHATBOT_SECOND_IFRAME="//*[@id='exw-conversation-frame']"
SIMGE_DURUMU_FRAME= ".exw-minimize-button > path:nth-child(2)"
KONUSMA_BITIRME_CSSSELECTOR=".exw-end-session-button > path"
SIMGE_DURUMU_CSSSELECTOR=".finishSessionCheckButtons > button:nth-child(1)"
LOGINBUTTON= "//*[@id='__next']/div/section[1]/nav/div/div/a[1]"


#login
LOGIN_URL="https://tobeto.com/giris"
LOGIN_BUTTON_XPATH="//button[contains(.,\'Giriş Yap\')]"
WARNING_MESSAGE_XPATH="//p[contains(.,\'Doldurulması zorunlu alan*\')]"
EPOSTA_TEXT_BOX_XPATH="//input[@name=\'email\']"
PASSWORD_TEXT_BOX_XPATH="//input[@name=\'password\']"
VALID_EPOSTA="elifisci1103@gmail.com"
VALID_PASSWORD="11d1103."
POPUP_MESSAGE_CSS=".toast-body"
POPUP_MESSAGE_POSITIVE= "• Giriş başarılı."
POPUP_MESSAGE_NEGATIVE="• Geçersiz e-posta veya şifre."
WARNING_MESSAGE="Doldurulması zorunlu alan*"
INVALID_PASSWORD="11E1103K"
INVALID_EPOSTA="elifisleyen743@gmail.com"
POPUP_MESSAGE_NEGATIVE2="• Henüz e-posta adresinizi doğrulamadınız."
name = "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input[1]"
password = "password"
PASSWORD_XPATH = "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input[2]"
password_input = "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input[2]"
LOGGİNBUTTON_XPATH= "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button"


#senkron
LESSONS = "//*[@id='lessons-tab']"
SHOWMORE_BUTTON = "//*[@id='lessons-tab-pane']/div/div/div[2]"
PROCEED_TO_TRAINING = "//*[@id='all-lessons-tab-pane']/div/div[14]/div/div[2]/a"
YOU_DID_IT = "#info-text-question > svg"
HOW_CAN_I_COMPLETE_TRANING = "//*[@id='info-text-question']/div/div[2]/div/div/p[1]"
HOW_CAN_I_ACHIEVE_TRANING = "//*[@id='info-text-question']/div/div[2]/div/div/p[2]"
LIKE_ICON = "main-content"
LIKE_NUMBER = "//*[@id='dynamicContent']/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div[3]/div/div/span[2]/span"
CLOSE_WINDOW= ".anticon-close path"
USER_CLICK = "#userCardPopover-13248 .col-lg-10"
FOLLOW_SHE = ".ant-btn-primary > span"
SUCCESSFUL_FOLLOW_MESSAGE = "//*[@id='wrapper-content']/div[2]/div/div/p"
CLOSE_MESSAGE = "//*[@id='growl-item-close']"
DONT_FOLLOW_SHE = ".ant-btn-primary > span"
UNSUCCESSFUL_FOLLOW_MESSAGE = ".growl-item-content > p"
CLOSE_UNSUCCESSFUL_FOLLOW_MESSAGE= "//*[@id='growl-item-close']"
FAVORI_ICON= "//*[@id='dynamicContent']/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div[4]/div/span"
FAVORI_ICON_MESSAGE = ".growl-item-content > p"

#takvim
LOGIN_URL="https://tobeto.com/giris"
CALENDAR_CSS=".calendar-btn"
CALENDAR_TEXT_XPATH="//span[text()='Eğitim ve Etkinlik Takvimi']"
SEARCH_EDUCATION_XPATH="//input[@placeholder='Eğitim arayın...']"
SEARCH_EDUCATION_TEXT="Yazılım Kalite ve Test"
QUALITY_TEST_XPATH="(//span[@class='text-truncate'])[1]"   
INSTRUCTOR_CLASS=" css-1xc3v61-indicatorContainer"
SEARCH_INSTRUCTOR_TEXT="İrem Balcı"
INSTRUCTOR_XPATH="(//span[@class='text-truncate'])[2]"
END_LESSONS_XPATH="//input[@name='eventEnded']"
CONTINUE_LESSONS_XPATH="//input[@name='eventContinue']"
BUY_LESSONS_XPATH="//input[@name='eventBuyed']"
NOT_STARTED_LESSONS_XPATH="//input[@name='eventNotStarted']"
MONTH_XPATH="//button[@title='Ay']"
WEEK_XPATH="//button[@title='Hafta']"
DAY_XPATH="//button[@title='Gün']"
RIGHT_KEYS_CLASS="//button[@title='ileri']"
LEFT_KEYS_CLASS="//button[@title='geri']"
CLOSE_BUTTON_XPATH="//button[@class='btn-close btn-close-white']"
CODE_ACADEMY_XPATH="(//a[text()='Codecademy'])[1]"

#eğitim/hayatım
#PROFİLEĞİTİMLERİM
MYEDUCATIONALİFE = "//*[@id='__next']/div/main/section/div/div/div[1]/div/a[3]/span[2]"
EGITIMDURUMU = "//label[@class='input-label-text' and text()='Eğitim Durumu*']"
UNIVERSITY = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/label"
MEZUNIYETYILI = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/label[1]"
BOLUM = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/label"
BASLANGICYILI = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/label"
SAVEBUTTON = "//*[@id='__next']/div/main/section/div/div/div[2]/form/button"
UNIVERSITY_FIELD = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/input"
EDUCATIONAL_STATUS = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/select"
SELECT_EDUCATIONAL_STATUS = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/select/option[4]"
ENAZIKIKARAKTER = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/span"
UMTFİFTY = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/span"
BOLUM_ENAZIKIKARAKTER = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/span"
BOLUM_ENFAZLAELLIKARAKTER = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/span"
START_YEAR = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/div[1]/div/input"
SELECTSTARTYEAR = ".react-datepicker__year-text:nth-child(9)"
GRADUATİON = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div[1]/div/input"
GRADUATİON_YEAR_CHECKBOX = "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/label[2]/input"
SELECT_GRADUATIONYEAR = ".react-datepicker__year-text:nth-child(10)"
FOR = ".react-datepicker__navigation--next"
BACK= ".react-datepicker__navigation"
START_2015 = ".react-datepicker__year-text:nth-child(11)"
MEZUNIYET_GERİGELME = ".react-datepicker-ignore-onclickoutside"
MEZUNIYETYILI_SECME = ".react-datepicker__year-text:nth-child(3)"
DELETE = "//*[@id='__next']/div/main/section/div/div/div[2]/div/div/div[2]/span"
ALERT_MESSAGE = "/html/body/div[4]/div/div/div/div/div/p[1]"
YES_BUTTON = "/html/body/div[4]/div/div/div/div/div/div[2]/button[2]"
PROFILE_XPATH = "//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button"
INFORMATİON_PROFILE= "//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a" 