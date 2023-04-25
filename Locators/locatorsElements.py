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
  
  yes_radio_xpath                  = '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]/label'
  impressive_radio_xpath           = '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/label'


class locatorsElementsWebTables():
  
  webTables_button_xpath                        = '#item-3 > span'
  searchBox_input_id                            = 'searchBox'
  delete_button_xpath                           = '//*[@id="delete-record-1"]'
  edit_button_xpath                             = '//*[@id="edit-record-3"]'

class locatorsElementsAddWebTables():
  
  add_button_id                                 = 'addNewRecordButton'
  firstName_text_id                             = 'firstName'
  lastName_text_id                              = 'lastName'
  userEmail_text_id                             = 'userEmail'
  age_text_id                                   = 'age'
  salary_text_id                                = 'salary'
  department_text_id                            = 'department'
  submit_button_id                              = 'submit'
  close_button_xpath                            = '/html/body/div[4]/div/div/div[1]/button/span[1]'