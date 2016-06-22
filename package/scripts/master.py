import sys, os, pwd, signal, time
from resource_management import *
from subprocess import call

class Master(Script):
  def install(self, env):
    # Install packages listed in metainfo.xml
    self.install_packages(env)
    self.configure(env)
    import params



  def configure(self, env):    
    import params
    import status_params    
    env.set_params(params)
    
    content=InlineTemplate(status_params.krb5_template_config)
    File(format("/etc/krb5.conf"), content=content, owner='root',group='root', mode=0644)
    

  def stop(self, env):
    import params
    import status_params
    self.configure(env)

          
  def start(self, env):
    import params
    import status_params
    self.configure(env)
    


  def status(self, env):
    import status_params
    env.set_params(status_params)  
  
    
if __name__ == "__main__":
  Master().execute()
