CREATE TABLE IF NOT EXISTS public.users (
    id          UUID    PRIMARY KEY     DEFAULT uuid_generate_v4(),

    external_id INTEGER NOT NULL,
    full_name   VARCHAR NOT NULL,

    created_at  TIMESTAMP WITHOUT TIME ZONE     NOT NULL    DEFAULT current_timestamp,
    updated_at  TIMESTAMP WITHOUT TIME ZONE     NOT NULL    DEFAULT current_timestamp
);

CREATE UNIQUE INDEX idx_id ON public.users (id);
CREATE INDEX idx_users ON public.users (external_id);

COMMENT ON TABLE public.users IS 'Пользователи';

COMMENT ON COLUMN public.users.id IS 'Идентификатор пользователя';

COMMENT ON COLUMN public.users.external_id IS 'Внешний ID';
COMMENT ON COLUMN public.users.full_name IS 'Полное имя';

COMMENT ON COLUMN public.users.created_at IS 'Дата создания';
COMMENT ON COLUMN public.users.updated_at IS 'Дата обновления';
