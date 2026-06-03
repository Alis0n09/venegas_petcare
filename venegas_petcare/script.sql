CREATE USER venegas_petcare_user WITH PASSWORD 'admin123';
CREATE DATABASE venegas_petcare_db OWNER venegas_petcare_user;

\c venegas_petcare_db

ALTER SCHEMA public OWNER TO venegas_petcare_user;
GRANT ALL ON SCHEMA public TO venegas_petcare_user;
GRANT CREATE ON SCHEMA public TO venegas_petcare_user;

ALTER DEFAULT PRIVILEGES FOR USER venegas_petcare_user IN SCHEMA public
GRANT ALL ON TABLES TO venegas_petcare_user;

ALTER DEFAULT PRIVILEGES FOR USER venegas_petcare_user IN SCHEMA public
GRANT ALL ON SEQUENCES TO venegas_petcare_user;

ALTER DEFAULT PRIVILEGES FOR USER venegas_petcare_user IN SCHEMA public
GRANT ALL ON FUNCTIONS TO venegas_petcare_user;

from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import EspeciesViewSet, MascotasViewSet
