from django.apps import AppConfig
class ProductAggregatorConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product_aggregator'

    def ready(self):
        import product_aggregator.signals  


    

     

        
              