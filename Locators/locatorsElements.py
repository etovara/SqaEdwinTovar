from selenium.webdriver.common.by import By

class locatorsElements():
  
  click_textbox_xpath           = '//*[@id="item-0"]/span'
  userName_textbox_id           = 'userName'
  email_textbox_id              = 'userEmail'
  currentAddress_textbox_id     = 'currentAddress'
  permanentAddress_textbox_id   = 'permanentAddress'
  submit_button_id              = 'submit'
  

class locatorsElementsCheckBox():
  
  checkbox_button_xpath             = '//*[@id="item-1"]/span'
  expand_button_css                 = '#tree-node > div > button.rct-option.rct-option-expand-all > svg'
  home_button_xpath                 = '//*[@id="tree-node"]/ol/li/span/label/span[3]'
  collapse_button_css               = '#tree-node > div > button.rct-option.rct-option-collapse-all > svg'


class locatorsElementsRadioButton():
  
  radio_button_xpath               = '//*[@id="item-2"]/span' 
  yes_radio_xpath                  = '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]/label' 
  impressive_radio_xpath           = ''