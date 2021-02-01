"""Test report serializers."""

import pytest
from ..serializers import ReportFileSerializer

@pytest.mark.django_db
def test_serializer_with_valid_date(report):
    """If a serializer has valid data it will return a valid object."""
    get_serializer = ReportFileSerializer(report)
    create_serializer = ReportFileSerializer(data=get_serializer.data)
    assert create_serializer.is_valid() is True

@pytest.mark.django_db
def test_serializer_increment_create(report):
    """Test serializer produces reports with correct version."""
    get_serializer = ReportFileSerializer(report)
    serializer_1 = ReportFileSerializer(data=get_serializer.data)
    assert serializer_1.is_valid() is True
    report_1 = serializer_1.save()

    serializer_2 = ReportFileSerializer(data=get_serializer.data)
    assert serializer_2.is_valid() is True
    report_2 = serializer_2.save()

    assert report_2.version == report_1.version + 1

