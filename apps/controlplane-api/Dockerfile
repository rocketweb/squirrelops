FROM python:3.12-slim AS runner

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /opt/controlplane

RUN apt-get update \
    && apt-get install -y --no-install-recommends gosu \
    && rm -rf /var/lib/apt/lists/*

COPY apps/controlplane-api/requirements.txt ./apps/controlplane-api/requirements.txt
COPY --from=pingting requirements.txt ./apps/controlplane-api/requirements-pingting.txt
RUN pip install --no-cache-dir \
    -r ./apps/controlplane-api/requirements.txt \
    -r ./apps/controlplane-api/requirements-pingting.txt

COPY adapters ./adapters
COPY config ./config
COPY scripts ./scripts
COPY harness ./harness
COPY apps/controlplane-api ./apps/controlplane-api

RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser && \
    chown -R appuser:appgroup /opt/controlplane

ENTRYPOINT ["/opt/controlplane/apps/controlplane-api/docker-entrypoint.sh"]
WORKDIR /opt/controlplane/apps/controlplane-api

EXPOSE 8199
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8199"]
