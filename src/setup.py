from setuptools import setup
import setup_translate

pkg = 'Extensions.MultiRC'
setup(name='enigma2-plugin-extensions-multirc',
       version='3.0',
       description='Use multiple Dreamboxes with different RCs',
       package_dir={pkg: 'MultiRC'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'maintainer.info']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
