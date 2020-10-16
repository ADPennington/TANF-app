import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
// import comboBox from 'uswds/src/js/components/combo-box'
import { fetchStts } from '../../actions/stts'
import Button from '../Button'
import ComboBox from '../ComboBox'

function EditProfile() {
  const stts = useSelector((state) => state.stts.stts)
  const dispatch = useDispatch()

  useEffect(() => {
    dispatch(fetchStts())
  }, [dispatch])

  return (
    <div className="grid-container">
      <h1 className="request-access-header font-serif-2xl">Request Access</h1>
      <p className="request-access-secondary">
        We need to collect some information before an OFA Admin can grant you
        access
      </p>
      <form className="usa-form">
        <label className="usa-label" htmlFor="first-name">
          First name
          <input
            className="usa-input"
            id="firstName"
            name="firstName"
            type="text"
            required
            aria-required="true"
          />
        </label>

        <label className="usa-label" htmlFor="lastName">
          Last name
          <input
            className="usa-input"
            id="lastName"
            name="lastName"
            type="text"
            required
            aria-required="true"
          />
        </label>
        <ComboBox sttList={stts} />
        <Button
          type="submit"
          disabled
          size="big"
          className="request-access-button"
        >
          Request Access
        </Button>
      </form>
    </div>
  )
}

export default EditProfile
